data = {
  usuarioIngresado: "eseizasantiao@gmail.com",
  contraseñaIngresada: "NoseProbemo",
};

fetch("http://0.0.0.0:8000/clientes/validarContraseña", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(data),
})
  .then((res) => res.json())
  .then((res) => console.log(res));
