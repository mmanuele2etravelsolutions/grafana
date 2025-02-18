from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Configurar el proveedor de trazas
tracer_provider = TracerProvider()
trace.set_tracer_provider(tracer_provider)

# Configurar el exportador de OpenTelemetry (OTLP)
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
span_processor = BatchSpanProcessor(otlp_exporter)
tracer_provider.add_span_processor(span_processor)

# Crear trazas de ejemplo
tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("mi_traza"):
    with tracer.start_as_current_span("subproceso"):
        print("Generando traza de ejemplo")

print("Trazas enviadas a Alloy")
