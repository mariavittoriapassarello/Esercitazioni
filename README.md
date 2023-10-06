# Esercitazioni
Nella directory PodmanLabs, sono contenuti i file:

1. graduates.py
2. requirements.txt
3. Containerfile

Dal terminale, per spostarsi nella Directory dove sono contenuti i file necessari:

```
cd PodmanLabs
```

Per creare la Container Image:

```
podman build -t prova .
```

Per creare un'istanza della Container Image:

```
podman run --rm --name container prova
```
