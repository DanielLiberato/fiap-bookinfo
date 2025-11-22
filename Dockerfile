# Usa uma imagem slim para ser leve
FROM python:3.9-slim

# Cria um diretório de trabalho
WORKDIR /app

# Instala as dependências
RUN pip install flask

# Copia o código
COPY productpage.py .

# SEGURANÇA: Cria um usuário não-root chamado 'appuser'
RUN useradd -m appuser
# Troca o dono dos arquivos para esse usuário
RUN chown -R appuser:appuser /app

# Muda para o usuário seguro
USER appuser

# Expõe a porta
EXPOSE 9080

# Roda a aplicação
CMD ["python", "productpage.py"]