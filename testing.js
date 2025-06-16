fetch("http://0.0.0.0:8000/autos/obtener")
  .then((res) => res.json())
  .then((res) => console.log(res));
