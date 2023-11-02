# AirFlowTutorial
## 專案名稱: AirFlowTutorial - NOTE
### 參考影片:**[coder2j - Airflow Tutorial for Beginners](https://www.youtube.com/watch?v=K9AnJ9_ZAXE&pp=ygUQYWlyZmxvdyB0dXRvcmlhbA%3D%3D)**
### 參考檔案:**[airflowZeroToHero.pdf](https://github.com/jerry7776112/AirFlowTutorial/blob/main/airflowZeroToHero.pdf)**

### Airflow YAML Download:**[AirflowYAML](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)**

### Apache-Airflow Introduction
* Apache Airflow 是一個開源的工作排程管理平台1，由 Airbnb 開發並於 2015 年開源1。它提供了多樣的 operator 可以使用，例如 Bash Operator、Python Operator，甚至可以直接對 GCP、S3、Slack 等等進行操作。
* **以下為 Apache Airflow 的特點**：
    * 提供了多樣的 operator 可以使用，例如 Bash Operator、Python Operator，甚至可以直接對 GCP、S3、Slack 等等進行操作。
    * 可以將有相關的工作整合為一個有向無循環圖 DAG（Directed Acyclic Graph），顧名思義就是有方向性且無回向造成循環的結構。
    * 整個 DAG 就是一個 Python 程式，達到大家所追求的 Infrastructure as code ，減少維運上的複雜度。
    * 提供了 Airflow Webserver、Airflow Scheduler 和 Airflow Worker 三個主要元件：
        * **Airflow Webserver**提供了方便的圖形化頁面，可以快速地看到排程執行的狀態，以及在上面查看 Log 或是手動觸發等。
        * **Airflow Scheduler** 負責排程，會持續監控所有的 DAG 與工作，當有符合條件的工作就會觸發使其執行。
        * **Airflow Worker** 實際的排程工作就是交由 Worker 來執行，同一個 Airflow cluster 中可以有多個 Worker，並且可通過指定 worker queue 使工作能在特定的資源上運作。

#### 實作
* Run Airflow in Docker
* Airflow DAG with Bash Operator
* Airflow DAG with Python Operator
* Data Sharing via Airflow Xcoms
* Airflow Task Flow API
* Airflow Catch-Up and Backfill
* Airflow Scheduler with Cron Expression

#### Docker Main Command
1. 下載 images
    * ```docker pull <images name>```
2. 啟動新的 container & 直接 pull images 後啟動 container
    * ```docker run <images name>```
3. 啟動另一個新的容器(d就是分離的意思)
    * ```docker run –d```
4. 綁定 image 端口
    * ```docker run-p<localPort>:<containerPort> <image>```
5. 綁定 image 端口並為 container 命名
    * ```docker run-p<localPort>:<containerPort> <named> <image>```
6. 指定啟動未運行的 container
    * ```docker start <id>```
7. 指定停止運行中的 container
    * ```docker stop <id>```
8. 列出當前運行中的 container
    * ```docker ps```
9. 列出當前所有存在的 container (不論是否運行中)
    * ```docker ps –a: ```
10. 查看 container 的狀態資訊
    * ```docker logs <Container ID or Names>: ```
11. 與 container 終端機互動
    * ```docker exec –it <Container ID>```
12. 建立自己的image 
    * ```docker build -t <image_name:tag> .```
    * t: 命名 
    * . :當前目錄
    * ex: docker build -t my-app:1.0 .
13. 刪除 container
    * ```docker rm <container ID>```
14. 刪除 image
    * ```docekr rmi <image name>```
15. 離開docker終端機
    * ```exit```
16. 執行.yaml
    * ```docker compose -f <.yaml> up```
    * -f : 指定要執行的檔案
    * up : 啟動
    * ex: docker compose -f mongo.yaml up
17. 關閉.yaml
    * ```docker compose -f <.yaml> down```
    * -f : 指定要執行的檔案
    * down : 關閉
    * ex: docker compose -f mongo.yaml down
