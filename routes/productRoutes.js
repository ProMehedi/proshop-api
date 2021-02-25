import express from 'express'
import {
  createProduct,
  deleteProductById,
  getProductById,
  getProducts,
  updateProduct,
} from '../controllers/productController.js'
import { isAdminUser, isLogin } from '../middleware/authMiddleware.js'

const router = express.Router()

// Fetch All Products
router.route('/').get(getProducts).post(isLogin, createProduct)

// Fetch & Delete & Update A Product By Id
router
  .route('/:id')
  .get(getProductById)
  .put(isLogin, isAdminUser, updateProduct)
  .delete(isLogin, isAdminUser, deleteProductById)

export default router
