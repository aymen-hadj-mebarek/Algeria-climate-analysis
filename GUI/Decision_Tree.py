import numpy as np

class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature=feature  
        self.threshold=threshold  
        self.left=left  
        self.right=right  
        self.value=value  

    def is_leaf_node(self):
        return self.value is not None

class DecisionTree:
    def __init__(self, min_samples_split=2, max_depth=100, n_features=None):
        self.min_samples_split=min_samples_split
        self.max_depth=max_depth
        self.n_features=n_features
        self.root=None

    def fit(self, X, y):
        X=np.array(X)
        y=np.array(y)
        self.n_features=X.shape[1] if not self.n_features else min(X.shape[1], self.n_features)
        self.root=self._grow_tree(X, y)

    def _grow_tree(self, X, y, depth=0):
        n_samples, n_feats=X.shape        
        if depth >= self.max_depth or n_samples < self.min_samples_split:
            leaf_value=self._most_common_label(y)
            return Node(value=leaf_value)

        feat_idxs=np.random.choice(n_feats, self.n_features, replace=False)        
        best_feature, best_thresh=self._best_split(X, y, feat_idxs)

        if best_feature is None:
            leaf_value=self._most_common_label(y)
            return Node(value=leaf_value)
        
        left_idxs, right_idxs=self._split(X[:, best_feature], best_thresh)
        left=self._grow_tree(X[left_idxs, :], y[left_idxs], depth + 1)
        right=self._grow_tree(X[right_idxs, :], y[right_idxs], depth + 1)
        return Node(best_feature, best_thresh, left, right)

    def _best_split(self, X, y, feat_idxs):
        best_gain=-1
        split_idx, split_threshold=None, None

        for feat_idx in feat_idxs:
            X_column=X[:, feat_idx]
            thresholds=np.unique(X_column)

            for thr in thresholds:                
                gain=self._variance_reduction(y, X_column, thr)

                if gain > best_gain:
                    best_gain=gain
                    split_idx=feat_idx
                    split_threshold=thr

        return split_idx, split_threshold

    def _variance_reduction(self, y, X_column, threshold):        
        parent_variance=np.var(y)
        
        left_idxs, right_idxs=self._split(X_column, threshold)

        if len(left_idxs) == 0 or len(right_idxs) == 0:
            return 0
        
        n=len(y)
        n_l, n_r=len(left_idxs), len(right_idxs)
        var_l, var_r=np.var(y[left_idxs]), np.var(y[right_idxs])
        weighted_variance=(n_l / n) * var_l + (n_r / n) * var_r
        
        variance_reduction=parent_variance - weighted_variance
        return variance_reduction

    def _split(self, X_column, split_thresh):
        left_idxs=np.argwhere(X_column <= split_thresh).flatten()
        right_idxs=np.argwhere(X_column > split_thresh).flatten()
        return left_idxs, right_idxs

    def _most_common_label(self, y):        
        return np.mean(y)

    def predict(self, X):
        X=np.array(X)
        return np.array([self._traverse_tree(x, self.root) for x in X])

    def _traverse_tree(self, x, node):
        if node.is_leaf_node():
            return node.value

        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)
        return self._traverse_tree(x, node.right)
