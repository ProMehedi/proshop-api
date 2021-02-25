import express from 'express'
import {
  deleteProductById,
  getProductById,
  getProducts,
} from '../controllers/productController.js'
import { isAdminUser, isLogin } from '../middleware/authMiddleware.js'

const router = express.Router()

// Fetch All Products
router.route('/').get(getProducts)

// Fetch & Delete & Update A Product By Id
router
  .route('/:id')
  .get(getProductById)
  .delete(isLogin, isAdminUser, deleteProductById)

export default router
