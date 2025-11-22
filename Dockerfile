FROM python:3.8-slim
WORKDIR /opt/microservices
COPY . .
# Simulação do Bookinfo para build rápido
RUN pip install flask requests
EXPOSE 9080
CMD ["python", "productpage.py"]