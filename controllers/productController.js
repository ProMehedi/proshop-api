import asyncHandler from 'express-async-handler'
import Product from '../models/productModel.js'

// @desc    Fetch All Products
// @route   GET /api/v1/products
// @access  Public
export const getProducts = asyncHandler(async (req, res) => {
  // Filter By Categories /api/v1/products?categories=ID1,ID2
  let filter = {}
  if (req.query.categories) {
    filter = { category: req.query.categories.split(',') }
  }

  const products = await Product.find(filter)

  if (products) {
    res.status(201).json(products)
  } else {
    res.status(404)
    throw new Error('Product Not Found!')
  }
})

// @desc    Fetch A Products
// @route   GET /api/v1/products/:id
// @access  Public
export const getProductById = asyncHandler(async (req, res) => {
  const product = await Product.findById(req.params.id)

  if (product) {
    res.json(product)
  } else {
    res.status(404)
    throw new Error('Product Not Found!')
  }
})

// @desc    Delete A Product By Id
// @route   DELETE /api/v1/products/:id
// @access  Private/Admin
export const deleteProductById = asyncHandler(async (req, res) => {
  const product = await Product.findById(req.params.id)

  if (product) {
    await product.remove()
    res.status(201).json({ success: true, message: 'Product Removed!' })
  } else {
    res.status(404)
    throw new Error('Product Not Found!')
  }
})
