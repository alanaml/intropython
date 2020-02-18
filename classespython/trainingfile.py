class TrainingMethod:
    def __init__(self, weight_to_lose, how_many_weeks, training_client):
        self.weight_to_lose = weight_to_lose
        self.how_many_weeks = how_many_weeks
        self.training_client = training_client

    def cal_per_day_to_ingest(self):
        return self.training_client.name


    def workout_per_day(self):
        pass
