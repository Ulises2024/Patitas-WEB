<h1> E-commerce Patitas </h1>
<h3>Este proyecto es una página web dinámica para la venta de productos para mascotas, desarrollada con Bootstrap en el frontend y Django en el backend. Utiliza SQLite3 como base de datos, gestionada a través de Django.
La aplicación ofrece diversas funcionalidades para e-commerce, destacando el desarrollo fullstack y la integración de APIs REST.
</h3>
<img src="https://github.com/Ulises2024/Patitas-WEB/blob/main/source_readme/pantalla_principal_patitas.png">
<hr>
<br>
<h2>1. Caso
</h2>
<p>
  Un grupo de amigas comenzó a realizar la venta de productos para mascotas como bandanas, correas e identificaciones, todo esto para ayudar a una fundación sin fines de lucro, todo partió a través de las redes sociales, pero en la actualidad es casi imposible dar abasto a la demanda a través de las redes sociales.
</p>
<p>
  Por eso, a contactado a los alumnos del Duoc para que puedan ayudarles a construir una aplicación web que permita a sus usuarios elaborar listas de compras con la intención de permitir a las amigas a ordenar sus presupuestos, mejorar sus finanzas, realizar el aporte a la fundación sin fines de lucro y mejorar la venta y el despacho de sus productos.
</p>
<h3>Los principales objetivos de la aplicación web son:</h3>
<ul>
  <li>Contar con una plataforma en internet para promover sus productos a usuarios registrados, que indique el stock real de productos disponibles</li>
  <li>Entregar el servicio venta en línea.</li>
  <li>Permitir al cliente para monitorear sus compras.</li>
  <li>Mejorar el proceso de logística de sus productos a los clientes mediante el seguimiento del despacho.</li>
  <li>Permitir generar descuentos o promociones en la página principal.</li>
  <li>Permitir subscribirse con una donación a la fundación sin fines de lucro, esta información ira directamente a la fundación. Con el fin de motivar a sus clientes, se otorgará un 5% de descuento en el total de la venta a todos los clientes que estén suscritos.</li>
</ul>
<h3>Funcionalidades del Sistema</h3>
<ul>
  <li>El sistema debe permitir registrar clientes para acceder a los servicios de ventas.</li>
  <li>El sistema debe permitir a los clientes generar una compra, descontando los productos del stock una vez creada la venta y realizar descuentos en caso de tratarse de una promoción o de un cliente suscrito.</li>
  <li>Para los usuarios registrados el sistema debe permitir ver un historial de ventas realizadas, además, del estado del despacho de las ventas.</li>
  <li>Mejorar el proceso de logística de sus productos a los clientes mediante el seguimiento del despacho.</li>
  <li>Para el despacho de los productos, el sistema WEB debe entregar una traza de seguimiento del despacho en el caso de los envíos a domicilio de clientes registrados, mostrando fecha y hora en que se toma el pedido, se despacha y es recibido por el cliente, cerrando el ciclo.</li>
  <li>El sistema debe permitir a los usuarios registrados poder subscribirse o des suscribirse de la donación a la fundación sin fines de lucro.</li>
  <li>Se deben crear mantenedores para la información relativa a clientes, usuarios, productos, promociones o descuentos.</li>
  <li>El sistema debe permitir mostrar las opciones de acuerdo con los perfiles de cada usuario.</li>
</ul>
<br>
<h2>2. Tecnologías utilizadas</h2>
<ul>
  <li><strong>Frontend:</strong> Bootstrap, HTML, CSS y JavaScript.</li>
  <li><strong>Backend:</strong> Python y Django.</li>
  <li><strong>Base de datos:</strong> SQLite3.</li>
  <li><strong>APIs:</strong> api.thecatapi.com, api.thedogapi.com y Mapbox Maps Service.</li>
  <li><strong>Otras:</strong> Git, Github y Trello.</li>

</ul>
<br>
<h2>3. Instalación y configuración</h2>
<p>Guía paso a paso para ejecutar el proyecto localmente.</p>
<ul>
  <li>1.- Clona este repositorio:<br>
  <pre>
    <code>git clone https://github.com/usuario/patitas-web.git  
    cd patitas-web</code>
  </pre>
  </li>
  <li>2.- Crea y activa un entorno virtual:<br>
  <pre>
    <code>python -m venv env  
    source env/bin/activate  # En Windows: env\Scripts\activate</code>
  </pre>
  </li>
  <li>3.- Instala las dependencias:<br>
  <pre>
    <code>pip install -r requisitos.txt</code>
  </pre>
  </li>
  <li>4.- Realiza las migraciones de la base de datos:<br>
  <pre>
    <code>python manage.py migrate</code>
  </pre>
  </li>
  <li>5.- Inicia el servidor:<br>
  <pre>
    <code>python manage.py runserver</code>
  </pre>
  </li>
  <p>Accede a la aplicación en tu navegador: http://127.0.0.1:8000.</p>
</ul>

