A mini real-time analytics project that simulates a pizza store chain and showcases the speed of ClickHouse for fast inserts & sub-10ms queries.

**🚀 What This Project Does**

-Generates live pizza orders using Python.

-Sends orders to Kafka.

-Consumers update order confirmation & completion events.

-Stores data in ClickHouse.

-Uses Materialized Views to maintain latest order status.

-Visualizes everything in Grafana.

-Achieves <116ms inserts and <10ms query latency on millions of rows.


**🧱 Tech Stack**

Python, Kafka, ClickHouse, Grafana, Materialized Views

**📊 Key Features**

-Real-time streaming ingestion

-High-speed OLAP queries

-Updated order lifecycle

-Grafana dashboard for monitoring

-220M rows read per hour benchmark

▶️ How to Run

-Start Kafka cluster

-Wake ClickHouse Service

-Run DB setup scripts

-Start order producer,order confirmation,order completion,increase inventory scripts at a time.

-Connect Grafana to ClickHouse
