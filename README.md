run: python3 calculator.py <ip> <port>


To check this send JSON:

{ 
  "operand1":<value>,
  "operand2":<value>,
  "operator":[+-*/]
}

curl --header "Content-Type: application/json" --request POST --data '{"operand1":"15", "operand2":"12", "operator":"*"}' http://<ip>:<port>

Answer format is JSON:

{
  "result":<value>
}
