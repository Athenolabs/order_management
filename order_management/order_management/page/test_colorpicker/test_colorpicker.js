frappe.pages['test-colorpicker'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Test Colorpicker',
		single_column: true
	});
	page.main.append(frappe.render_template('test_colorpicker', {"name": frappe.user.name}))
	page.main.find('#my-colorpicker').colorpicker({
							position: {
								my: 'center',
								at: 'center',
								of: page.main.find('#my-colorpicker')
							},
							modal: true
						});;
}
