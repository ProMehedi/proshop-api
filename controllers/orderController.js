import asyncHandler from 'express-async-handler'
import Order from '../models/orderModel.js'

// @desc    Fetch All Orders
// @route   GET /api/v1/orders
// @access  Private/Admin
export const getOrders = asyncHandler(async (req, res) => {
  const orders = await Order.find({}).populate(
    'user',
    '-password -createdAt -updatedAt'
  )

  if (orders) {
    res.status(201).json(orders)
  } else {
    res.status(404)
    throw new Error('No Order Found!')
  }
})

// @desc    Fetch Login User Orders
// @route   GET /api/v1/orders/myorders
// @access  Private
export const getMyOrders = asyncHandler(async (req, res) => {
  const orders = await Order.find({ user: req.user._id })

  if (orders) {
    res.status(201).json(orders)
  } else {
    res.status(404)
    throw new Error('No Order Found!')
  }
})

// @desc    Get A Order By ID
// @route   POST /api/v1/orders/:id
// @access  Private
export const getOrderById = asyncHandler(async (req, res) => {
  const order = await Order.findById(req.params.id).populate(
    'user',
    'name email address'
  )

  if (order) {
    res.status(201).json(order)
  } else {
    res.status(404)
    throw new Error('Order not found!')
  }
})

// @desc    Create New Order
// @route   POST /api/v1/orders
// @access  Private
export const addNewOrder = asyncHandler(async (req, res) => {
  const {
    orderItems,
    shippingAddress,
    paymentMethod,
    itemsPrice,
    taxPrice,
    shippingPrice,
    totalPrice,
  } = req.body

  if (orderItems && orderItems.length === 0) {
    res.status(400)
    throw new Error('No order items')
  } else {
    const order = new Order({
      orderItems,
      user: req.user._id,
      shippingAddress,
      paymentMethod,
      itemsPrice,
      taxPrice,
      shippingPrice,
      totalPrice,
    })

    const createOrder = await order.save()

    res.status(201).json(createOrder)
  }
})

// @desc    Update A Order to Paid
// @route   PUT /api/v1/orders/:id/pay
// @access  Private
export const updateOrderToPaid = asyncHandler(async (req, res) => {
  const order = await Order.findById(req.params.id)

  if (order) {
    order.isPaid = true
    order.paidAt = Date.now()
    order.paymentResult = {
      id: req.body.id,
      status: req.body.status,
      update_time: req.body.update_time,
      // email_address: req.body.payer.email_address,
    }

    const updatedOrder = await order.save()
    res.status(201).json(updatedOrder)
  } else {
    res.status(404)
    throw new Error('Order not found!')
  }
})

// @desc    Update A Order to Delivered
// @route   PUT /api/v1/orders/:id/deliver
// @access  Private
export const updateOrderToDelivered = asyncHandler(async (req, res) => {
  const order = await Order.findById(req.params.id)

  if (order) {
    order.isDelivered = true
    order.deliveredAt = Date.now()

    const updatedOrder = await order.save()
    res.status(201).json(updatedOrder)
  } else {
    res.status(404)
    throw new Error('Order not found!')
  }
})
