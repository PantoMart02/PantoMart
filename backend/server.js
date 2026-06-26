require('dotenv').config();

const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();

// ======================
// ✅ MIDDLEWARE
// ======================
app.use(cors());
app.use(express.json());

// Serve static files (images, css, etc.)
app.use('/assets', express.static('assets'));

// ======================
// ✅ DATABASE CONNECTION (FIXED)
// ======================
mongoose.connect(process.env.MONGO_URI)
.then(() => console.log("✅ MongoDB Connected"))
.catch(err => console.error("❌ MongoDB Error:", err));

// ======================
// ✅ PRODUCT MODEL
// ======================
const productSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    price: {
        type: Number,
        required: true
    },
    category: {
        type: String,
        required: true,
        lowercase: true
    },
    image: {
        type: String,
        default: "/assets/images/placeholder.jpg"
    },
    images: {
        type: [String],
        default: []
    },
    description: {
        type: String,
        default: ""
    },
    benefits: {
        type: [String],
        default: []
    },
    usage: {
        type: String,
        default: ""
    },
    subcategory: {
        type: String,
        default: "Exclusive Addition"
    }
}, { timestamps: true });

const Product = mongoose.model('Product', productSchema);

// ======================
// ✅ ROUTES
// ======================

// ROOT
app.get('/', (req, res) => {
    res.send("🚀 API Running Successfully");
});

// GET ALL PRODUCTS
app.get('/products', async (req, res) => {
    try {
        const products = await Product.find().sort({ createdAt: -1 });
        res.json(products);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// GET PRODUCTS BY CATEGORY  ← must be before /:id
app.get('/products/category/:name', async (req, res) => {
    try {
        const category = req.params.name.toLowerCase();
        const products = await Product.find({ category });
        res.json(products);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// GET SINGLE PRODUCT
app.get('/products/:id', async (req, res) => {
    try {
        const product = await Product.findById(req.params.id);

        if (!product) {
            return res.status(404).json({ message: "Product not found" });
        }

        res.json(product);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// ADD PRODUCT (TEST)
app.post('/products', async (req, res) => {
    try {
        const newProduct = new Product(req.body);
        await newProduct.save();

        res.json({
            message: "✅ Product added successfully",
            product: newProduct
        });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// DELETE PRODUCT
app.delete('/products/:id', async (req, res) => {
    try {
        await Product.findByIdAndDelete(req.params.id);
        res.json({ message: "🗑️ Product deleted" });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// ======================
// ✅ SERVER START
// ======================
const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
    console.log(`🚀 Server running on port ${PORT}`);
});