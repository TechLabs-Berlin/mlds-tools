### Instructions
Place all your configs in this folder. They will not be pushed to github and can only be modified locally. For an example on how to do this, see the data back-ends workshop [here](../README.md#firebase).

For all workshop purposes, the correct configuration requirea a single JSOn file name `app_creds.json` to be present in this directory. The contents of the file should look something like this:
```json
{
  "type": "service_account",
  "project_id": "save-nyc-demo",
  "private_key_id": "37uiewof8f09486912g34g5678g9fde0e897io28973172",
  "private_key": "-----BEGIN PRIVATE KEY-----\nruewyqihfwcnqrfjiurhr923y923897288329hdnoiurh3dur2ehwuiwhiwuhuihruiwhriuwheuh\nhOnHAlulPq8kHrbC8qz4t8jg8vCx/mLh4knhHzWZDbyEENZxkJdlr+pdYoSrw7S\nB2lz01JucB8gDHFhheWz4OfqAmPZz3HFfMv7BNgbcq594dl5foap/qxSWDl+0pdU\nmazdJyDLAgMBAAECggEAFJEptzVACQbpl4JclmrVkNFfFCs9crVvBQKt6cLAPfn7\niJ0zcUPBsJWBoMPqzAXZp/xUDZWJpAFFao2VElLJW3J3EZVriKuIkMQLTpN0IuCE\n8T/cB7j0zUAFaNDsZuIrz+1zBZ0W/Alta5jJi7ornM0oOTOtW3zruewyqihfwcnqrfjiurhr923y923897288329hdnoiurh3dur2ehwuiwhiwuhuihruiwhriuwheuh\nhOnHAlulPq8kHrbC8qz4t8jg8vCx/mLh4knhHzWZDbyEENZxkJdlr+pdYoSrw7S\nB2lz01JucB8gDHFhheWz4OfqAmPZz3HFfMv7BNgbcq594dl5foap/qxSWDl+0pdU\nmazdJyDLAgMBAAECggEAFJEptzVACQbpl4JclmrVkNFfFCs9crVvBQKt6cLAPfn7\niJ0zcUPBsJWBoMPqzAXZp/xUDZWJpAFFao2VElLJW3J3unyklYWSNF1S8D5gDbCE90YAul4dfYBR\n1ngYK1c9S97V9yCI8NfqWm2WaQKBgQC8JEgrY1obmxmraWf35/hsfiazj7tnUE6C\n9jcs8P3BbcdK8FHmnbfxUm+3xseWLB+I7uVQCukt37fVebnCFy65P69X39/6IXTF\n1pts9QAZ7tSaXI5RV3ZrJL4K1i9d0TXc4WDi/pWu185CJIaPKlpuyocpVKC334lN\nf5S8XBRfEwKBgFRFqjAr4P7gxOey51xTP51U8iTFxSeqQ98R5pM2//aE+wgE/S5I\n5LVBIBygYmf8C1/ZuPUUc6ybm2gNmVyqzA9Dicncq0HbaLrxkOAVqz5uoL1GzCQT\npp6OGKEc0kC56xSoXRuEfAKuG9/+mZnygbCbDAcEtYrCzd2oazZ44DyBAoGAMrwx\n/glPvkwIExJcqByVAGTQePGUntqoIWbWIDdopqW87Xd7Do6PkPMjD1L6dYO2iU2q\n5vfaQ7WltFqb/jwULH6BAVhs5N3qyIMD7NDw0w11pZ65/jNwypng6bkyksEdHlBk\nuTHgGYM2qt2Ar9DDDEdvRXT91jfgpdZ2vIi0MaMCgYAcH+uvwhHh/E7YoIg9ficx\n838JRSq3yjEbBdWEMFzhJaJRpm3zjutSkw40SzfLeHFaO6ET7sLwsblmjNU+0KEM\nUS4To8OBbzHlnCtTcflkw9n5EoTexiqCSPxIxwdTubKk+ufaUyDXz1CmmW2qMPwf\nZ2cYXVRQmYkIB/VAtPI9HQ==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-z1234@save-nyc-demo.iam.gserviceaccount.com",
  "client_id": "1000000000000000001",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-z1234%40save-nyc-demo.iam.gserviceaccount.com"
}
```