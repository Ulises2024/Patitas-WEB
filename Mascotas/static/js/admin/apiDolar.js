window.addEventListener('DOMContentLoaded', (event) => {
    fetch('https://v6.exchangerate-api.com/v6/839d7c43be8c9551c8ce0478/latest/USD') // Reemplaza YOUR-API-KEY con tu clave de API
      .then(response => response.json())
      .then(data => {
        // Manipula los datos recibidos de la API
        const dolarValue = data.conversion_rates.CLP; // Reemplaza MXN con el código de la moneda deseada

        // Muestra la información en la página
        const dolarElement = document.getElementById('dolar');
        dolarElement.textContent = `El valor del dólar hoy: ${dolarValue} pesos`;
      })
      .catch(error => {
        console.log('Error al obtener el valor del dólar:', error);
      });
  });

  window.addEventListener('DOMContentLoaded', (event) => {
    fetch('https://mindicador.cl/api') // URL de la API de Mindicador.cl para obtener los indicadores económicos
      .then(response => response.json())
      .then(data => {
        // Manipula los datos recibidos de la API
        const ufValue = data.uf.valor;
        const ipcValue = data.ipc.valor;
        const utmValue = data.utm.valor;

        // Muestra la información en la página
        const ufElement = document.getElementById('uf');
        ufElement.textContent = `Valor de la UF hoy: ${ufValue} pesos`;

        const ipcElement = document.getElementById('ipc');
        ipcElement.textContent = `Valor del IPC hoy: ${ipcValue}%`;

        const utmElement = document.getElementById('utm');
        utmElement.textContent = `Valor del UTM hoy: ${utmValue} pesos`;
      })
      .catch(error => {
        console.log('Error al obtener los indicadores económicos:', error);
      });
  });