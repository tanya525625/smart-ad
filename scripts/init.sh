chmod +x export_virtvars.sh
wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
chmod +x cloud_sql_proxy
sudo mkdir /cloudsql
sudo chown -R $USER /cloudsql
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt