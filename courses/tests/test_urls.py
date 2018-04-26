from django.urls import reverse, resolve
from courses.urls import urlpatterns

class TestUrls:

	
	def test_list_url(self):
		path = reverse('courses:list')
		resolver = resolve(path)
		assert resolve(path).url_name == 'list'
		assert resolve(path).view_name == 'courses:list'
	
	def test_details_url(self):
		path = reverse('courses:detail', args=[1])
		resolver = resolve(path)
		assert resolve(path).url_name == 'detail'
		assert resolve(path).view_name == 'courses:detail'

	def test_new_url(self):
		path = reverse('courses:new')
		resolver = resolve(path)
		assert resolve(path).url_name == 'new'
		assert resolve(path).view_name == 'courses:new'

	def test_edit_url(self):
		path = reverse('courses:edit', args=[1])
		resolver = resolve(path)
		assert resolve(path).url_name == 'edit'
		assert resolve(path).view_name == 'courses:edit'

	def test_delete_url(self):
		path = reverse('courses:delete', args=[1])
		resolver = resolve(path)
		assert resolve(path).url_name == 'delete'
		assert resolve(path).view_name == 'courses:delete'