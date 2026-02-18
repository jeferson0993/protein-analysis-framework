# protein-analysis-framework
Framework Genérico de Análise Proteica Multi-Etapas, totalmente neutro, educacional e reutilizável para:

- Análise de proteomas
- Filtragem multicritério
- Ranking ponderado automático
- Construção de construct proteico genérico
- Predição estrutural (ESMFold opcional)
- Geração automática de relatório estilo artigo
- Docker multi-stage otimizado
- CLI profissional com argparse
- Logging estruturado

### Estrutura do Projeto
```sh
protein-analysis-framework/
│
├── app/
│   ├── cli.py
│   ├── pipeline.py
│   ├── stage1_processing.py
│   ├── stage2_analysis.py
│   ├── stage3_construct.py
│   ├── ranking.py
│   ├── structure.py
│   ├── report.py
│   ├── config.py
│   └── utils.py
│
├── data/
├── results/
├── logs/
│
├── requirements.txt
├── Dockerfile
└── docker-compose.yml

```

### Execução
- Build
```sh
docker build -t protein-framework .
```
- Run
```sh
docker run -v $(pwd)/data:/app/data \
           -v $(pwd)/results:/app/results \
           protein-framework \
           --input data/example.fasta \
           --structure \
           --report
```
- Output
```sh
results/
├── final_construct.fasta
└── report.pdf
```
