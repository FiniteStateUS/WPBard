import requests

def get_bard_response(query):
  response = requests.get("https://bard.ai/api/v1/generate", params={"query": query})
  return response.json()

def wpb_bard_widget():
  """A WordPress widget that displays Bard responses."""
  query = "<input type='text' name='query' />"
  response = get_bard_response(query)
  output = response["text"]
  return """
    <div>
      <h2>Bard</h2>
      <p>Enter a query below to get a response from Bard.</p>
      {query}
      <p>{output}</p>
    </div>
  """.format(query=query, output=output)

def wpb_bard_frame():
  """A WordPress frame that displays Bard responses."""
  query = "<input type='text' name='query' />"
  response = get_bard_response(query)
  output = response["text"]
  return """
    <iframe src="https://bard.ai/frame?query={query}"></iframe>
  """.format(query=query)

def wpb_bard_init():
  """Registers the Bard widget and frame."""
  register_widget("wpb_bard_widget")
  register_frame("wpb_bard_frame")

if __name__ == "__main__":
  wpb_bard_init()
