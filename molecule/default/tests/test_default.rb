# frozen_string_literal: true

describe file('/etc/sudoers.d/dmesg') do
  it { should exist }
end

describe file('/root/.bashrc') do
  it { should exist }
end

describe file('/root/.bash_profile') do
  it { should exist }
end
