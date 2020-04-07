export GOOGLE_APPLICATION_CREDENTIALS=./account/key.json
export CLOUD_SQL_CONNECTION_NAME='smartyad:europe-west2:statistic'
./cloud_sql_proxy -dir=/cloudsql --instances=$CLOUD_SQL_CONNECTION_NAME --credential_file=$GOOGLE_APPLICATION_CREDENTIALS