import express from 'express'
import {
  addNewOrder,
  getMyOrders,
  getOrderById,
  getOrders,
  updateOrderToPaid,
} from '../controllers/orderController.js'
import { isAdminUser, isLogin } from '../middleware/authMiddleware.js'

const router = express.Router()

// Get Login User Orders
router.route('/myorders').get(isLogin, getMyOrders)

// Get A Order By ID
router.route('/:id').get(isLogin, getOrderById)

// Create New Order
router
  .route('/')
  .get(isLogin, isAdminUser, getOrders)
  .post(isLogin, addNewOrder)

// Get A Order By ID
router.route('/:id/pay').put(isLogin, updateOrderToPaid)

export default router
