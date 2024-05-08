import express from 'express';
import { promisify } from 'util';
import { createClient } from 'redis';

const app = express();
const client = createClient();
const port = 1245;

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

//promisifies client.get function
const get = promisify(client.get).bind(client);

const listProducts = [
  { 'itemId': 1, 'itemName': 'Suitcase 250', 'price': 50, 'initialAvailableQuantity': 4},
  { 'itemId': 2, 'itemName': 'Suitcase 450', 'price': 100, 'initialAvailableQuantity': 10},
  { 'itemId': 3, 'itemName': 'Suitcase 650', 'price': 350, 'initialAvailableQuantity': 2},
  { 'itemId': 4, 'itemName': 'Suitcase 1050', 'price': 550, 'initialAvailableQuantity': 5}
];

//retrieve item by id/data access
function getItemById(id) {
  return listProducts.filter((item) => item.itemId === id)[0];
}

function reserveStockById(itemId, stock) {
  client.set(itemId, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await get(itemId);
  return stock;
}

app.get('/list_products', function (request, respond) {
  respond.json(listProducts);
});

app.get('/list_products/:itemId', async function (request, respond) {
  const itemId = req.params.itemId;
  const item = getItemById(parseInt(itemId));
  
app.get('/reserve_product/:itemId', async function (request, respond) {
  const itemId = req.params.itemId;
  const item = getItemById(parseInt(itemId));

  if (!item) {
    res.json({"status": "Product not found"});
    return;
  }

//set up express server
app.listen(port, () => {
  console.log(`app listening at http://localhost:${port}`);
});
