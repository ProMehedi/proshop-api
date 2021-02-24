import express from 'express'
import {
  addNewOrder,
  getMyOrders,
  getOrderById,
  updateOrderToPaid,
} from '../controllers/orderController.js'
import { isLogin } from '../middleware/authMiddleware.js'

const router = express.Router()

// Get Login User Orders
router.route('/myorders').get(isLogin, getMyOrders)

// Get A Order By ID
router.route('/:id').get(isLogin, getOrderById)

// Create New Order
router.route('/').post(isLogin, addNewOrder)

// Get A Order By ID
router.route('/:id/pay').put(isLogin, updateOrderToPaid)

export default router
