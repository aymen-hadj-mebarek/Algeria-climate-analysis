from PyQt5 import QtCore
from Decision_Tree import DecisionTree
from PyQt5.QtWidgets import QMessageBox
from Random_Forest import RandomForest
from DBSCAN import *
from CLARANS import *
class ModelTrainingWorker(QtCore.QObject):
    finished = QtCore.pyqtSignal(object)  # Signal to notify that training is finished and pass the trained model

    def __init__(self, params, loading_dialog):
        super().__init__()
        self.params = params
        self.loading_dialog = loading_dialog

    def run(self):
        # Training logic goes here, which could take some time
        trained_model = None
        try:
            if self.params["name"] == "Decision Tree":
                # print(self.params)
                X = self.params["x_train"]
                y = self.params["y_train"]

                # Create and train the Decision Tree
                decision_tree = DecisionTree(
                    min_samples_split=self.params.get("min_samples_split", 2),
                    max_depth=self.params.get("max_depth", 100)
                )
                decision_tree.fit(X, y)

                # Save the trained model to pass it to the main thread
                trained_model = decision_tree
                
            elif self.params["name"] == "Random Forest":
                # print(self.params)
                X = self.params["x_train"]
                y = self.params["y_train"]
                print(self.params.get("n_trees", 20))
                print(self.params.get("min_samples_split", 2))
                print(self.params.get("max_depth", 100))
                print("start training")
                # Create and train the Decision Tree
                random_forest = RandomForest(
                    n_trees= self.params.get("n_trees", 20),
                    min_samples_split=self.params.get("min_samples_split", 2),
                    max_depth=self.params.get("max_depth", 100)
                )
                random_forest.fit(X, y)

                # Save the trained model to pass it to the main thread
                trained_model = random_forest
                print("finish training")
            elif self.params["name"] == "DBSCAN" :
                
                data_clustering = self.params['x_train']
                dbscan_labels = dbscan_algo(data_clustering, 
                                            eps = self.params.get("eps",0.6), 
                                            min_samples=self.params.get("min_sample",5))

                final_result = self.params['x_train'].copy()
                final_result['Target'] = self.params['y_train']
                final_result['Clusters'] = dbscan_labels
                dataset = final_result.copy()
                final_result = final_result.groupby('Clusters').mean()
                
                trained_model = {
                    'dataset':dataset,
                    'final_data': final_result
                }
                print(final_result)
                
            elif self.params["name"] == "CLARANS" :
                data_clustering_values = self.params['x_train'].values

                # Obtenir les meilleurs médodes, le coût et les clusters
                best_medoids, best_clusters, labels, noise = clarans_algo(data_clustering_values, 
                                                                 number_clusters=self.params.get("number_clusters",5), 
                                                                 max_neighbors=self.params.get("max_neighbors",10), 
                                                                 num_local=self.params.get("num_local",10))

                # Générer les labels de CLARANS, où chaque point de données est attribué au cluster de son medoid le plus proche
                clarans_labels = labels
                    
                final_result = self.params['x_train'].copy()
                final_result['Target'] = self.params['y_train']
                final_result['Clusters'] = clarans_labels
                dataset = final_result.copy()
                final_result = final_result.groupby('Clusters').mean()
                
                trained_model = {
                    'dataset':dataset,
                    'final_data': final_result,
                    'clusters': best_clusters,
                    'best_medoids': best_medoids,
                    'noise':noise
                }
                
        except:
            QMessageBox.critical(None, "Error", f"Error while loading data or features or target")

        # Emit signal to notify that training is finished and pass the model
        self.finished.emit(trained_model)
