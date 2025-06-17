diccionarioVenta = {
  data: {
    medio_de_pago: "transferencia",
    cuotas: false,
    cantidad: null,
    codigo_vs: 5782,
    codigo_pv: null,
    precio: 20000.0,
  },
  correo_electronico: "santiagoeseiza10@gmail.com",
};

fetch("http://0.0.0.0:8000/ventas/confimarMail", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(diccionarioVenta),
})
  .then((res) => res.json())
  .then((res) => console.log(res));
