from src.MoviesRecom.entity.config_entity import DataTransformationConfig
import os
import pandas as pd
import ast


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    # fun for getting names {genre, keywords}

    def convert_01(self, text):
        L = []
        for i in ast.literal_eval(text):
            L.append(i['name'])
        return L

    # fun for getting 3 names of actors

    def Act_names(self, text):
        names = []
        c = 0
        for i in ast.literal_eval(text):
            if c < 3:
                names.append(i['name'])
            c += 1
        return names

    # fun for getting names of directors

    def fetch_director(self, text):
        names = []
        for i in ast.literal_eval(text):
            if i['job'] == 'Director':
                names.append(i['name'])
        return names

    def prepare_data(self):
        movies = pd.read_csv(self.config.movies_path)
        # logger.info(movies.head(2))
        credits = pd.read_csv(self.config.credits_path)
        # logger.info(credits.head(2))

        # merge movies and credits
        df = movies.merge(credits, on='title')

        # getting only useful columns
        df = df[['movie_id', 'title', 'overview',
                 'genres', 'keywords', 'cast', 'crew']]

        # removing null valuse
        df = df.dropna()

        # getting only names from genres and
        df['genres'] = df['genres'].apply(self.convert_01)
        df['keywords'] = df['keywords'].apply(self.convert_01)

        # Getting 3 actors or actresses names for each movie
        df['cast'] = df['cast'].apply(self.Act_names)

        # Getting name of the movie director
        df['crew'] = df['crew'].apply(self.fetch_director)

        # Removing space b/w names for example
        df['crew'] = df['crew'].apply(
            lambda x: [i.replace(" ", "") for i in x])
        df['genres'] = df['genres'].apply(
            lambda x: [i.replace(" ", "") for i in x])
        df['keywords'] = df['keywords'].apply(
            lambda x: [i.replace(" ", "") for i in x])
        df['cast'] = df['cast'].apply(
            lambda x: [i.replace(" ", "") for i in x])

        # spliting overview
        df['overview'] = df['overview'].apply(lambda x: x.split(' '))

        # combine columns
        df['tags'] = df.overview + df.genres + df.keywords + df.cast + df.crew

        # remove the columns
        df = df.drop(
            ['overview', 'genres', 'keywords', 'cast', 'crew'], axis=1)

        # join tags columns each string
        df['tags'] = df['tags'].apply(lambda x: " ".join(x))

        # save the dataset
        df.to_csv(os.path.join(self.config.root_dir,
                  'clean_df.csv.'), index=False)
