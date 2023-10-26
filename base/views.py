from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product, Category
from rest_framework import status


# Create your views here.
class ProductListViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        """List product instances.

        Args:
            self: The instance of the view class.
            request: The HTTP request object containing request parameters.
            *args: Variable-length positional arguments.
            **kwargs: Variable-length keyword arguments.

        Returns:
            Response: An HTTP response containing a list of serialized product instances.

        This method is used to retrieve a list of product instances and serialize them using the
        ProductSerializer. The serialized data is then returned in an HTTP response.

        Note:
        - Ensure that the appropriate HTTP method (e.g., GET) is used for retrieving the list of products.
        - The 'request' parameter may contain query parameters or other information for filtering or
        customizing the list of products.
        - This function is typically used as part of a Django REST framework API view for listing products.
        """
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """Create a new Product.

        Args:
            request (Request): The HTTP request object containing the data for creating the Product.
            *args: Variable-length positional arguments.
            **kwargs: Variable-length keyword arguments.

        Returns:
            Response: A response containing the created Product data or error messages.

        This method is used to delete a product instance. First, it checks if the user is authenticated.
        If the user is not authenticated, a 401 Unauthorized response is returned, indicating that
        login is required.

        This function is responsible for creating a new Product based on the data provided in the request. It performs the following steps:

        1. Deserialize the request data using the ProductSerializer.
        2. Check if the 'category' field is provided in the request data.
        3. If 'category' is provided, it attempts to find the corresponding Category object in the database.
        4. If the Category object does not exist, a 400 Bad Request response is returned.
        5. If the serializer is valid and the Category object exists, the Product is created with the current user as the 'by' field.
        6. The function returns a response with the created Product data if successful, or validation errors if there are any issues.

        Raises:
            HTTP_401_UNAUTHORIZED: If the user is not AUTHORIZED.
            HTTP_400_BAD_REQUEST: If there are validation errors or the 'category' does not exist in the database.
            HTTP_201_CREATED: If the Product is successfully created.


        Example:
        ```
        POST /api/products/
        {
            "name": "Product Name",
            "description": "Product description.",
            "category": "Category Name",
            "mrp": 100,
            "discount": 10
        }

        Returns:

        HTTP 201 Created
        {
            "id": 1,
            "name": "Product Name",
            "description": "Product description.",
            "category": "Category Name",
            "mrp": 100,
            "discount": 10
        }
        """
        if not request.user.is_authenticated:
            return Response(
                {"Login": "Login required."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        serializer = ProductSerializer(data=request.data)

        category = request.data.get("category")
        if category is not None:
            try:
                category = Category.objects.get(name=category)
            except Category.DoesNotExist:
                return Response(
                    {"category": "Category does not exist in the database."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        if serializer.is_valid():
            serializer.save(by=request.user, category=category)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """Update an existing product instance.

        Args:
            self: The instance of the view class.
            request: The HTTP request object containing the updated data.
            *args: Variable-length positional arguments.
            **kwargs: Variable-length keyword arguments.

        Returns:
            Response: An HTTP response containing the updated product data or error messages.

        This method is used to delete a product instance. First, it checks if the user is authenticated.
        If the user is not authenticated, a 401 Unauthorized response is returned, indicating that
        login is required.

        This method is used to update an existing product instance with the data provided in the
        HTTP request. It first retrieves the instance to be updated, and if a 'category' field is
        included in the request data, it checks if the specified category exists in the database.
        If the 'category' is provided and doesn't exist, an error response is returned.

        Then, the request data is deserialized using the ProductSerializer, and if the data is valid,
        the product instance is updated with the new data, and the updated product data is returned
        in the response. If there are validation errors, an error response with the validation errors
        is returned.

        Note:
        - Make sure to use the appropriate HTTP method (e.g., PUT or PATCH) for updating the product.
        - The 'request' parameter should contain the data for the product update.
        - This function is typically used as part of a Django REST framework API view for product updates.


        Raises:
            HTTP_401_UNAUTHORIZED: If the user is not AUTHORIZED.
            HTTP_400_BAD_REQUEST: If there are validation errors or the 'category' does not exist in the database.
            HTTP_201_CREATED: If the Product is successfully created.


        Example:
        ```
        PUT /api/products/id
        {
            "id": 1
            "name": "Product Name",
            "description": "Product description.",
            "category": "Category Name",
            "mrp": 100,
            "discount": 10
        }

        Returns:

        HTTP 201 Created
        {
            "id": 1,
            "by: "user"
            "name": "Product Name",
            "description": "Product description.",
            "category": "Category Name",
            "mrp": 100,
            "discount": 10
        }

        """
        if not request.user.is_authenticated:
            print("\n\nYes\n\n")
            return Response(
                {"Login": "Login required."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        instance = self.get_object()
        category = request.data.get("category")

        if category is not None:
            try:
                category = Category.objects.get(name=category)
            except Category.DoesNotExist:
                return Response(
                    {"category": "Category does not exist in the database."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        serializer = ProductSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save(category=category)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """Delete a product instance.

        Args:
            self: The instance of the view class.
            request: The HTTP request object containing the request information.
            *args: Variable-length positional arguments.
            **kwargs: Variable-length keyword arguments.

        Returns:
            Response: An HTTP response indicating the result of the delete operation.

        This method is used to delete a product instance. First, it checks if the user is authenticated.
        If the user is not authenticated, a 401 Unauthorized response is returned, indicating that
        login is required.

        If the user is authenticated, the product instance is retrieved using the 'get_object' method
        (presumably from a Django REST framework viewset), and then it is deleted. A 204 No Content
        response is returned to indicate a successful deletion with no content in the response body.

        Note:
        - Ensure that the appropriate HTTP method (e.g., DELETE) is used for deleting the product.
        - This function is typically used as part of a Django REST framework API view for deleting products.
        - Make sure to use proper authentication mechanisms before accessing this endpoint.
        """
        if not request.user.is_authenticated:
            return Response(
                {"Login": "Login required."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        # Custom logic to delete a Product
        instance = self.get_object()
        if not instance:
            pass

        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
