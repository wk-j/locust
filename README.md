## Locust

```bash
python3 -m pip install locustio
locust --host=http://localhost:5000  -f src/test.py
open http://localhost:8089
```

## Service

```bash
dotnet new webapi --language C# --out src/MyWeb
dotnet run --project src/MyWeb
open http://localhost:5000/WeatherForecast
```

## Wrk

```bash
brew install wrk
wrk -t200 -c400 -d30s http://localhost:5000/WeatherForecast
```