# Hosting DeepSeek R1 Locally on macOS with Docker

## **1. Install Docker on macOS**
Download and install **Docker Desktop** from:
- [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/)

Once installed, enable **Rosetta for x86 compatibility** (for Apple Silicon users):

```sh
softwareupdate --install-rosetta
```

---

## **2. Check GPU Support (Apple Silicon & Intel Mac)**
- **Apple Silicon (M1/M2/M3)**: Docker **does not** support direct GPU acceleration for AI models. DeepSeek R1 will run **on CPU only** (very slow performance).
- **Intel Mac**: If you have an eGPU, GPU support is still limited in Docker on macOS.

---

## **3 Docker Login**
Run the following command in **`Terminal`**:

`Authenticate` with `Github` or `Google` or `any other SSO provider`

```sh
docker login
```
Once docker login is done then you can pull the images.
---


---

## **3.1 Pull the DeepSeek R1 Docker Image**
Run the following command in **Terminal**:

`Need to  review this step`

```sh
docker pull deepseek-ai/deepseek-llm:latest
```
`Couldn't find the above repo. `Please use the following

```sh
docker pull aixblock/deepseek-r1:latest
```
---

## **4. Run the Container**
Since macOS does not support **GPU acceleration in Docker**, run DeepSeek R1 using **CPU only**:

```sh
docker run -it --rm -p 8080:80 deepseek-ai/deepseek-llm
```

Run the container with the latest image pulled from the above source

```sh
docker run -it --rm -p 8080:80 deepseek-ai/deepseek-llm
```

**Flags explanation:**
- `-it` → Runs in interactive mode.
- `--rm` → Removes the container after exiting.
- `-p 8080:80` → Maps the container's API to port 8080 on your Mac.

**⚠ Note:** Running on CPU will be **very slow**. Consider running DeepSeek R1 on a **Linux machine** or **cloud service** for better performance.

---

## **5. Access DeepSeek R1**
Once running, open your browser and go to:

```
http://localhost:8080
```

Or, test it using **cURL**:

```sh
curl -X POST "http://localhost:8080/api" -H "Content-Type: application/json" -d '{"prompt": "Hello, AI!", "max_tokens": 100}'
```

---

## **6. Run in Background (Detached Mode)**
To keep DeepSeek R1 running in the background:

```sh
docker run -d -p 8080:80 --name deepseek-r1 deepseek-ai/deepseek-llm
```

To check running containers:

```sh
docker ps
```

To stop the container:

```sh
docker stop deepseek-r1
```

---

## **7. Alternative: Run with Docker Compose**
Create a `docker-compose.yml` file:

```yaml
version: '3'
services:
  deepseek-r1:
    image: deepseek-ai/deepseek-llm:latest
    ports:
      - "8080:80"
    restart: unless-stopped
```

Then, start the service:

```sh
docker-compose up -d
```

---

## **8. Next Steps (For Better Performance)**
Since **macOS lacks GPU support for AI models in Docker**, consider:
- Running DeepSeek R1 on a **Linux machine with NVIDIA GPU**.
- Using **cloud services** like Google Cloud, AWS, or Lambda Labs.
- Running a **smaller model** like `deepseek-coder` for CPU-friendly performance.

---

### **That's it! 🚀**
Now you have DeepSeek R1 running locally on macOS with Docker! Let me know if you need help. 😊


# Uninstall

## Uninstall

## To uninstall (remove) the deepseek-r1 Docker image from your system, you can follow these steps:

Stop any running containers using the deepseek-r1 image:
```sh
docker stop deepseek-r1 || echo "Container deepseek-r1 not running"
```

Remove the stopped container:
```sh
docker rm deepseek-r1 || echo "Container deepseek-r1 does not exist"
```

Remove the Docker image:
```sh
docker rmi aixblock/deepseek-r1:latest
```
List all Docker images to verify removal:

```sh
docker images
```

These commands will stop and remove any running containers using the deepseek-r1 image and then remove the image itself from your Docker environment.