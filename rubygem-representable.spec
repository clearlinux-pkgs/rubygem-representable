#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-representable
Version  : 3.0.0
Release  : 6
URL      : https://rubygems.org/downloads/representable-3.0.0.gem
Source0  : https://rubygems.org/downloads/representable-3.0.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-bundler
BuildRequires : rubygem-json
BuildRequires : rubygem-minitest
BuildRequires : rubygem-mongoid
BuildRequires : rubygem-multi_json
BuildRequires : rubygem-nokogiri
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-ruby-prof
BuildRequires : rubygem-test_xml
BuildRequires : rubygem-uber
BuildRequires : rubygem-virtus

%description
# Representable
Representable maps Ruby objects to documents and back.
[![Gitter Chat](https://badges.gitter.im/trailblazer/chat.svg)](https://gitter.im/trailblazer/chat)
[![Build
Status](https://travis-ci.org/apotonick/representable.svg)](https://travis-ci.org/apotonick/representable)
[![Gem Version](https://badge.fury.io/rb/representable.svg)](http://badge.fury.io/rb/representable)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n representable-3.0.0
gem spec %{SOURCE0} -l --ruby > rubygem-representable.gemspec

%build
export LANG=C
gem build rubygem-representable.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
representable-3.0.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/representable-3.0.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/CHANGES.md
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/README.md
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/TODO
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/TODO.getting_serious
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/autoload.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/binding.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/cached.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/coercion.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/config.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/debug.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/declarative.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/decorator.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/definition.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/deserializer.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/for_collection.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/hash.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/hash/allow_symbols.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/hash/binding.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/hash/collection.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/hash_methods.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/insert.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/json.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/json/collection.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/json/hash.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/object.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/object/binding.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/pipeline.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/pipeline_factories.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/populator.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/represent.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/serializer.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/xml.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/xml/binding.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/xml/collection.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/xml/hash.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/yaml.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/lib/representable/yaml/binding.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/representable.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/as_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/benchmarking.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/binding_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/cached_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/class_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/coercion_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/config/inherit_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/config_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/decorator_scope_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/decorator_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/default_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/defaults_options_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/definition_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/example.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/examples/object.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/exec_context_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/features_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/filter_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/for_collection_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/generic_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/getter_setter_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/hash_bindings_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/hash_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/heritage_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/if_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/include_exclude_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/inherit_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/inline_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/instance_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/is_representable_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/json_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/lonely_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/mongoid_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/nested_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/object_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/parse_pipeline_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/pipeline_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/populator_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/prepare_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/private_options_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/reader_writer_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/realistic_benchmark.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/render_nil_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/represent_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/representable_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/schema_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/serialize_deserialize_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/skip_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/stringify_hash_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/test_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/test_helper_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/uncategorized_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/user_options_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/wrap_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/xml_bindings_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/xml_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/representable-3.0.0/test/yaml_test.rb
/usr/lib64/ruby/gems/2.3.0/specifications/representable-3.0.0.gemspec
