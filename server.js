import express from 'express'
import dotenv from 'dotenv'
import colors from 'colors'
import productRoutes from './routes/productRoutes.js'
import connectDB from './config/db.js'
import * as errorMiddleware from './middleware/errorMiddleware.js'

// Initialize Dotenv
dotenv.config()

// Connect MongoDB
connectDB()

// Initialize The Express
const app = express()

// Define Variables
const api = process.env.API_URL || '/api/'
const port = process.env.PORT || 5000

app.get('/', (req, res) => {
  res.send('Server is ready!')
})

app.use(`${api}/products`, productRoutes)

// Custom Error Handling
app.use(errorMiddleware.notFound)
app.use(errorMiddleware.errorHandler)

// Initialize The Server
app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`.yellow.bold)
})
