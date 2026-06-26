require('dotenv').config();
const mongoose = require('mongoose');
const fs = require('fs');
const path = require('path');

// ======================
// ✅ CONNECT DATABASE
// ======================
mongoose.connect(process.env.MONGO_URI)
  .then(() => console.log("✅ MongoDB Connected for Seeding"))
  .catch(err => console.error("❌ MongoDB Error:", err));


// ======================
// ✅ PRODUCT SCHEMA
// ======================
const productSchema = new mongoose.Schema({
  name: String,
  price: Number,
  category: String,
  mainImage: String,
  description: String,
  benefits: [String],
  rating: Number,
  reviewsCount: Number
});

const Product = mongoose.model('Product', productSchema);


// ======================
// ✅ LOAD JSON FILE
// ======================
const productsFile = path.join(__dirname, 'products.json');

const seedProducts = async () => {
  try {
    const data = fs.readFileSync(productsFile, 'utf-8');
    const products = JSON.parse(data);

    // ❌ Clear old data (important)
    await Product.deleteMany();
    console.log("🗑️ Old products removed");

    // ✅ Insert new data
    await Product.insertMany(products);
    console.log("🌱 Products seeded successfully");

    process.exit();
  } catch (err) {
    console.error("❌ Seeding error:", err);
    process.exit(1);
  }
};

seedProducts();