data = {
  usuarioIngresado: "administracionViajes@gmail.com",
  contraseñaIngresada: "contraseñaDeLaAdministracion",
};

fetch("http://0.0.0.0:8000/clientes/validarContraseñaAdmin", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(data),
})
  .then((res) => res.json())
  .then((res) => console.log(res));
