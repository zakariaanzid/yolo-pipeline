from kfp.client import Client


with open("/var/run/secrets/kfp/token", "r") as f:
    token = f.read().strip()

client = Client(
    host="https://kns-job-1.jxe.10.132.0.56.nip.io/pipeline",
    verify_ssl=False,
    namespace="zakaria",
    existing_token=token
)

yolo_experiment = client.create_experiment(name="YOLO Experiments")

run = client.create_run_from_pipeline_package(
    pipeline_file="pipeline.yaml",
    arguments={
        "batch": 8,
        "data_pvc_name": "yolo-data-small",
        "data_source": "/data/yolo/fire-smoke-small/fire_smoke_small.yaml",
        "imgsz": 704,
        "model_source": "yolov8n.pt",
        "nb_epochs": 2,
        "output_pvc_name": "yolo-output-small"
    },
    run_name="yolo-train-small",
    experiment_id="YOLO Experiments"
)






