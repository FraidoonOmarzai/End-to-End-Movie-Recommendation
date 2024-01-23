from src.MoviesRecom.config.configuration import ConfigurationManager
from src.MoviesRecom.components.model_training import ModelTraining
from src.MoviesRecom.logging import logger


STAGE_NAME = 'Model Training'


class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_train_config = config.get_model_train_config()
        model = ModelTraining(model_train_config)
        model.bag_of_words()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(
            f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
