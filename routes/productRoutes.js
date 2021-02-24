import express from 'express'
import {
  getProductById,
  getProducts,
} from '../controllers/productController.js'

const router = express.Router()

// Fetch All Products
router.route('/').get(getProducts)

// Fetch A Product By Id
router.route('/:id').get(getProductById)

export default router
