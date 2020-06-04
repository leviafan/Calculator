import http.server
import json
import re
import sys

class CalcServerHandler(http.server.BaseHTTPRequestHandler):

  def check_posted_data(self, parsed_json):
    print(parsed_json)
    if parsed_json['operand1'] is None:
      return False

    if parsed_json['operand2'] is None:
      return False

    if not (parsed_json['operator'] in ('+', '-', '*', '/')):
      print(2)
      return False

    if re.fullmatch('\d+', parsed_json['operand1']) is None:
      print(3)
      return False
    if re.fullmatch('\d+', parsed_json['operand2']) is None:
      print(4)
      return False

    return True


  def do_GET(self):
    self.send_response(400)
    self.end_headers()

  def do_POST(self):
    if self.headers['Content-type'] == 'application/json':
      content_length = int(self.headers['Content-Length'])
      data = self.rfile.read(content_length)
      parsed_json = json.loads(data)
      print(type(parsed_json))

    else:
      self.send_response(400)
      self.end_headers()

    if self.check_posted_data(parsed_json):
      if parsed_json['operator'] == '+':
        result = int(parsed_json['operand1']) + int(parsed_json['operand2'])
      elif parsed_json['operator'] == '-':
        result = int(parsed_json['operand1']) - int(parsed_json['operand2'])
      elif parsed_json['operator'] == '*':
        result = int(parsed_json['operand1']) * int(parsed_json['operand2'])
      elif parsed_json['operator'] == '/':
        result = int(parsed_json['operand1']) / int(parsed_json['operand2'])

      result_text = json.dumps({'result': result}) + "\n"
      self.send_response(200)
      self.send_header('Content-type', 'application/json')
      self.end_headers()
      self.wfile.write(result_text.encode())


    else:
      self.send_response(400)
      print('Not_checked')
      self.end_headers()


if __name__ == '__main__':
  host = sys.argv[1]
  port = int(sys.argv[2])
  
  server = http.server.HTTPServer((host, port), CalcServerHandler)
  server.serve_forever()

