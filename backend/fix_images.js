/**
 * fix_images.js
 * Updates mainImage paths in MongoDB to use the correct file extensions
 * based on what actually exists in the frontend assets folder.
 */
require('dotenv').config();
const mongoose = require('mongoose');
const path = require('path');
const fs = require('fs');

const FRONTEND_ASSETS = path.join(__dirname, '..', 'PantoMart', 'assets', 'images', 'products');

const productSchema = new mongoose.Schema({
  name: String,
  price: Number,
  category: String,
  image: String,
  mainImage: String,
  images: [String],
  description: String,
  benefits: [String],
  usage: String,
  subcategory: String,
  rating: Number,
  reviewsCount: Number
}, { timestamps: true });

const Product = mongoose.model('Product', productSchema);

function findActualExtension(category, number) {
  const folder = path.join(FRONTEND_ASSETS, category);
  if (!fs.existsSync(folder)) return null;

  const files = fs.readdirSync(folder);
  // Look for files matching the number (e.g. "1.webp", "1.jpg", "1.png")
  const match = files.find(f => {
    const base = path.basename(f, path.extname(f));
    return base === String(number);
  });
  return match ? path.extname(match) : null;
}

async function fixImages() {
  await mongoose.connect(process.env.MONGO_URI);
  console.log('✅ Connected to MongoDB');

  const products = await Product.find();
  console.log(`📦 Found ${products.length} products`);

  let fixed = 0;
  let skipped = 0;

  for (const product of products) {
    const current = product.mainImage || '';
    // Extract category and number from path like /assets/images/products/care/1.jpg
    const match = current.match(/\/assets\/images\/products\/(\w+)\/(\d+)\.\w+/);
    if (!match) {
      console.log(`⏭️  Skipping ${product.name} — path: ${current}`);
      skipped++;
      continue;
    }

    const [, category, number] = match;
    const ext = findActualExtension(category, number);

    if (!ext) {
      console.log(`⚠️  No file found for ${category}/${number} (${product.name})`);
      skipped++;
      continue;
    }

    const newPath = `/assets/images/products/${category}/${number}${ext}`;

    if (newPath === current) {
      skipped++;
      continue;
    }

    await Product.updateOne({ _id: product._id }, { $set: { mainImage: newPath } });
    console.log(`✅ ${product.name}: ${current} → ${newPath}`);
    fixed++;
  }

  console.log(`\n✅ Done. Fixed: ${fixed}, Skipped: ${skipped}`);
  mongoose.disconnect();
}

fixImages().catch(err => {
  console.error('❌ Error:', err);
  process.exit(1);
});
