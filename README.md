# Product Manager by. Bram Steenbergen N. Matricola: 282839

This webservice allows for the management of a simple database containing products through the django framework. This branch will reply with XML files and requires information to be passed via http's POST system.

This webservice uses the Django framework to handle requests, based on a pre-established url scheme configured inside django like this:

hostname/admin shows the django build in administration application.<br>
hostname/products allows for the manipluation of the products database. <br>

Both the "admin" and "products" applications have sub-url's but here we will be focusing purely on the "products" application:

*products/addproduct* Allows you to add a product to the list. <br>
*products/listproducts* Lists all products in the database. <br>
*products/getproduct/<ID>* Lists a single product in the database. <br>
*products/updateproduct/<ID>* Allows you to update a specified product via POST function. <br>
*products/deleteproduct/<ID>* Allows you to delete a specified product. <br>
