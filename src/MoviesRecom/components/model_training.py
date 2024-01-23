from src.MoviesRecom.config.configuration import ModelTrainingConfig
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.MoviesRecom.logging import logger
from src.MoviesRecom.utils.common import save_bin
import pandas as pd
import joblib
import os


class ModelTraining:
    def __init__(self, config: ModelTrainingConfig) -> None:
        self.config = config
        self.df = pd.read_csv(self.config.df_path)

    def bag_of_words(self):
        cv = CountVectorizer(max_features=5000, stop_words='english')
        vector = cv.fit_transform(self.df['tags']).toarray()
        similarity = cosine_similarity(vector)

        # save_bin(similarity, os.path.join(self.config.root_dir, self.config.model_name))
        joblib.dump(similarity, os.path.join(
            self.config.root_dir, self.config.model_name))
