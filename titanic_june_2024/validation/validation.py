

from mlflow.models import make_metric, MetricThreshold

def validation_thresholds():
    return {
        "accuracy_score": MetricThreshold(
            threshold=0.75, higher_is_better=True  
        )
    }



