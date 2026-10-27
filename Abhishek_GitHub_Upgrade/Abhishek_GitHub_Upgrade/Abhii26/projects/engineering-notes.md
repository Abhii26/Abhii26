# Engineering notes

Selected professional work described in my resume. These notes summarize contributions; they do not publish employer source code.

## Group-photo recognition

Worked on offline classroom attendance with Flutter, ONNX, SCRFD, and ArcFace. Optimizations included preprocessing in worker isolates, batched embeddings, ONNX thread tuning, and fewer SAHI tiles.

| Reported measurement | Before | After |
| --- | --- | --- |
| Group-photo processing time | 210 s | 150 s |
| SAHI tiles | 36 | 16 |

The processing-time reduction is approximately 28.6%, rounded to 29%. Tile count fell by approximately 55.6%, rounded to 56%.

These are observations from the measured workload, not a guarantee for every image or device. Hardware, input dimensions, face count, run count, and timing boundaries are not specified in this public summary. Recognition accuracy requires a separate labeled evaluation; similarity scores alone do not establish accuracy.

## Selfie attendance

Implemented on-device selfie recognition measured under 3 seconds, offline storage, retry-based synchronization, and timestamp checks using NTP, a monotonic clock, and reboot detection. The timing applies to the measured recognition workflow and is not presented as a server-sync SLA.

## Edge inference

Built a detection and re-identification pipeline on Jetson Orin using YOLOv8, BoT-SORT, FAISS, and TensorRT. Batched inference processed three RTSP feeds, with results and CPU/GPU metrics exposed through FastAPI.

[Back to profile](../README.md)
