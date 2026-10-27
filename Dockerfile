FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PORT=8000
EXPOSE 8000
# threads (not just workers) so streaming replies don't block other users
CMD ["sh", "-c", "gunicorn run:app -b 0.0.0.0:${PORT} --workers 2 --threads 16 --timeout 180"]
