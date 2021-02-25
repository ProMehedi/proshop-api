import express from 'express'
import {
  addNewOrder,
  getMyOrders,
  getOrderById,
  getOrders,
  updateOrderToPaid,
  updateOrderToDelivered,
} from '../controllers/orderController.js'
import { isAdminUser, isLogin } from '../middleware/authMiddleware.js'

const router = express.Router()

// Get Login User Orders
router.route('/myorders').get(isLogin, getMyOrders)

// Get A Order By ID
router.route('/:id').get(isLogin, getOrderById)

// Get/Create/Update Order
router
  .route('/')
  .get(isLogin, isAdminUser, getOrders)
  .post(isLogin, addNewOrder)

// Update A Order to paid
router.route('/:id/pay').put(isLogin, updateOrderToPaid)

// Update A Order to Delivered
router.route('/:id/deliver').put(isLogin, isAdminUser, updateOrderToDelivered)

export default router
