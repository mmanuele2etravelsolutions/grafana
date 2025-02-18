🔹 Explicación del setup

Alloy: Actúa como colector de métricas y logs.
Prometheus: Se encarga de recolectar métricas desde Alloy.
Grafana: Visualiza los datos de Alloy desde Prometheus.
Loki: Permite almacenar y consultar logs recolectados por Alloy.

1. Instalar el SDK de OpenTelemetry en Python

pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp-proto-grpc
pip install opentelemetry-instrumentation-logging

2.
python trace_test.py

3.
Visualizar en Grafana
Abre Grafana en http://localhost:3000.
Ir a Explore → Selecciona Tempo como fuente de datos.
Busca las trazas ejecutando consultas como:
{trace_id="<ID-DE-LA-TRAZA>"}