from src.MoviesRecom.utils.common import *
from src.MoviesRecom.constants import *
from src.MoviesRecom.entity.config_entity import (DataIngestionConfig,
                                                  DataValidationConfig,
                                                  DataTransformationConfig,
                                                  ModelTrainingConfig)


class ConfigurationManager:
    def __init__(self, config_file=CONFIG_PATH):
        self.config_path = read_yaml(config_file)
        create_directories([self.config_path.artifacts_root])

    def dataIngestionConfig(self) -> DataIngestionConfig:
        config = self.config_path.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            data_url=config.data_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config

    def get_data_validation(self) -> DataValidationConfig:
        config = self.config_path.data_validation
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            unzip_dir=config.unzip_dir,
            status=config.status
        )
        return data_validation_config

    def get_data_transofrmation_config(self) -> DataTransformationConfig:
        config = self.config_path.data_transformation
        create_directories([config.root_dir])

        data_transofrmation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            movies_path=config.movies_path,
            credits_path=config.credits_path,
        )
        return data_transofrmation_config

    def get_model_train_config(self) -> ModelTrainingConfig:
        config = self.config_path.model_training
        create_directories([config.root_dir])

        model_train_config = ModelTrainingConfig(
            root_dir=config.root_dir,
            df_path=config.df_path,
            model_name=config.model_name
        )
        return model_train_config
