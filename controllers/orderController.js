import asyncHandler from 'express-async-handler'
import Order from '../models/orderModel.js'

// @desc    Get Order By ID
// @route   POST /api/v1/orders/:id
// @access  Private
export const getOrderById = asyncHandler(async (req, res) => {
  const order = await Order.findById(req.params.id).populate(
    'user',
    'name email address'
  )

  if (order) {
    res.json(order)
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
